import itertools
import sys
import copy


from crossword import Variable, Crossword


class CrosswordCreator():

    def __init__(self, crossword):
        """
        Create new CSP crossword generate.
        """
        self.crossword = crossword
        self.domains = {
            var: self.crossword.words.copy()
            for var in self.crossword.variables
        }

    def letter_grid(self, assignment):
        """
        Return 2D array representing a given assignment.
        """
        letters = [
            [None for _ in range(self.crossword.width)]
            for _ in range(self.crossword.height)
        ]
        for variable, word in assignment.items():
            direction = variable.direction
            for k in range(len(word)):
                i = variable.i + (k if direction == Variable.DOWN else 0)
                j = variable.j + (k if direction == Variable.ACROSS else 0)
                letters[i][j] = word[k]
        return letters

    def print(self, assignment):
        """
        Print crossword assignment to the terminal.
        """
        letters = self.letter_grid(assignment)
        for i in range(self.crossword.height):
            for j in range(self.crossword.width):
                if self.crossword.structure[i][j]:
                    print(letters[i][j] or " ", end="")
                else:
                    print("█", end="")
            print()

    def save(self, assignment, filename):
        """
        Save crossword assignment to an image file.
        """
        from PIL import Image, ImageDraw, ImageFont
        cell_size = 100
        cell_border = 2
        interior_size = cell_size - 2 * cell_border
        letters = self.letter_grid(assignment)

        # Create a blank canvas
        img = Image.new(
            "RGBA",
            (self.crossword.width * cell_size,
             self.crossword.height * cell_size),
            "black"
        )
        font = ImageFont.truetype("assets/fonts/OpenSans-Regular.ttf", 80)
        draw = ImageDraw.Draw(img)

        for i in range(self.crossword.height):
            for j in range(self.crossword.width):

                rect = [
                    (j * cell_size + cell_border,
                     i * cell_size + cell_border),
                    ((j + 1) * cell_size - cell_border,
                     (i + 1) * cell_size - cell_border)
                ]
                if self.crossword.structure[i][j]:
                    draw.rectangle(rect, fill="white")
                    if letters[i][j]:
                        w, h = draw.textsize(letters[i][j], font=font)
                        draw.text(
                            (rect[0][0] + ((interior_size - w) / 2),
                             rect[0][1] + ((interior_size - h) / 2) - 10),
                            letters[i][j], fill="black", font=font
                        )

        img.save(filename)

    def solve(self):
        """
        Enforce node and arc consistency, and then solve the CSP.
        """
        self.enforce_node_consistency()
        self.ac3()
        return self.backtrack(dict())

    def enforce_node_consistency(self):
        """
        Update `self.domains` such that each variable is node-consistent.
        (Remove any values that are inconsistent with a variable's unary
         constraints; in this case, the length of the word.)
        """
        for variable, words in self.domains.copy().items():
            for word in words.copy():
                if variable.length != len(word):
                    self.domains[variable].remove(word)

    def revise(self, x, y):
        """
        Make variable `x` arc consistent with variable `y`.
        To do so, remove values from `self.domains[x]` for which there is no
        possible corresponding value for `y` in `self.domains[y]`.

        Return True if a revision was made to the domain of `x`; return
        False if no revision was made.
        """
        revised = False
        overlap = self.crossword.overlaps[x, y]
        # No overlap -> X does not influence Y
        if overlap is None:
            return revised
        for word in self.domains[x].copy():
            if not self.constraint(word, y, overlap):
                self.domains[x].remove(word)
                revised = True
        return revised

    def constraint(self, word, y, overlap):
        """
        check if word satisfies constraint for (word, Y)

        Return True if constraint is satisfied; 
        return False if not satisfied
        """
        for y_word in self.domains[y]:
            if word != y_word and word[overlap[0]] == y_word[overlap[1]]:
                return True
        return False


    def ac3(self, arcs=None):
        """
        Update `self.domains` such that each variable is arc consistent.
        If `arcs` is None, begin with initial list of all arcs in the problem.
        Otherwise, use `arcs` as the initial list of arcs to make consistent.

        Return True if arc consistency is enforced and no domains are empty;
        return False if one or more domains end up empty.
        """
        if arcs is None:
            arcs = list(itertools.permutations(self.domains.keys(), 2))
            arcs = [arc for arc in arcs if arc[0] != arc[1] and self.crossword.overlaps[arc[0], arc[1]] is not None]

        while arcs:
            (x, y) = arcs.pop(0)
            if self.revise(x, y):
                if not self.domains[x]:
                    return False
                # update all neighbors becuase Xdomain got changed
                for z in self.crossword.neighbors(x) - {y}: arcs.append((z, x))
                   
        return True

    def assignment_complete(self, assignment):
        """
        Return True if `assignment` is complete (i.e., assigns a value to each
        crossword variable); return False otherwise.
        """
        for variable in self.crossword.variables:
            if not variable in assignment or assignment[variable] is None:
                return False
        return True

    def consistent(self, assignment):
        """
        Return True if `assignment` is consistent (i.e., words fit in crossword
        puzzle without conflicting characters); return False otherwise.
        """
        #check unique values
        if len(set(val for val in assignment.values())) != len(assignment):
            return False
        # check len(value) == variable.length
        for variable, value in assignment.items():
            if len(value) != variable.length: 
                return False
        # check no conflicts between neighbors
        neighbors = {var: self.crossword.neighbors(var) for var in assignment.keys()}
        for var, var_neighbors in neighbors.items():
            for neighbor in var_neighbors:
                i, j = self.crossword.overlaps[var, neighbor]
                if neighbor in assignment.keys() and assignment[var][i] != assignment[neighbor][j]:
                    return False    
        return True

    def order_domain_values(self, var, assignment):
        """
        Return a list of values in the domain of `var`, in order by
        the number of values they rule out for neighboring variables.
        The first value in the list, for example, should be the one
        that rules out the fewest values among the neighbors of `var`.
        """
        values_keys = {value: 0 for value in list(self.domains[var])}
        for value in values_keys:
            if value in assignment:
                continue
            else:
                for neighbor in self.crossword.neighbors(var):
                    if not neighbor in assignment:
                        i, j = self.crossword.overlaps[var, neighbor]
                        for neighbor_value in self.domains[neighbor]:
                            if value[i] != neighbor_value[j]:
                                values_keys[value] += 1
        return sorted(values_keys, key=lambda x: values_keys[x])
        

    def select_unassigned_variable(self, assignment):
        """
        Return an unassigned variable not already part of `assignment`.
        Choose the variable with the minimum number of remaining values
        in its domain. If there is a tie, choose the variable with the highest
        degree. If there is a tie, any of the tied variables are acceptable
        return values.
        """
        # all unassigned variables
        unas_variables = []
        for var in self.crossword.variables:
            if var not in assignment.keys():
                unas_variables.append(var)

        # get degree of given variable
        def degree(var):
            return len(self.crossword.neighbors(var))

        # get domain size of var
        def domain_size(var):
            return len(self.domains[var])

        # sort by degree and domain size
        sorted_variables = sorted(sorted(unas_variables, key=degree, reverse=True), key=domain_size)

        return sorted_variables[0] if sorted_variables else None



    def backtrack(self, assignment):
        """
        Using Backtracking Search, take as input a partial assignment for the
        crossword and return a complete assignment if possible to do so.

        `assignment` is a mapping from variables (keys) to words (values).

        If no assignment is possible, return None.
        """
        if self.assignment_complete(assignment):
            return assignment
        var = self.select_unassigned_variable(assignment)
        for value in self.order_domain_values(var, assignment):
            test_assignment = assignment.copy()
            test_assignment.update({var: value})

            if self.consistent(test_assignment):
                assignment.update({var: value})
                result = self.backtrack(assignment)
                if result is not None:
                    return result
                del assignment[var]
        return None
                

def main():

    # Check usage
    if len(sys.argv) not in [3, 4]:
        sys.exit("Usage: python generate.py structure words [output]")

    # Parse command-line arguments
    structure = sys.argv[1]
    words = sys.argv[2]
    output = sys.argv[3] if len(sys.argv) == 4 else None

    # Generate crossword
    crossword = Crossword(structure, words)
    creator = CrosswordCreator(crossword)

    assignment = creator.solve()

    # Print result
    if assignment is None:
        print("No solution.")
    else:
        creator.print(assignment)
        if output:
            creator.save(assignment, output)


if __name__ == "__main__":
    main()
