from logging import NullHandler
import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    if len(corpus) == 0:
        raise Exception('No files in corpus')

    dic_prob_next_page = {}
    if len(corpus[page]):   
        prob_all_pages = (1 - damping_factor) / len(corpus)
        for filename in corpus:
            if filename in corpus[page]:
                dic_prob_next_page.update({filename: damping_factor / len(corpus[page]) + prob_all_pages})
            else:
                dic_prob_next_page.update({filename: prob_all_pages})
    else:
        for filename in corpus:
            dic_prob_next_page.update({filename: 1 / len(corpus)})

    return dic_prob_next_page


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    pagerank = {}
    # choose first sample
    sample = random.choice(list(corpus))
    pagerank.update({sample: 1})

    for i in range(n-1):
        model = transition_model(corpus, sample, damping_factor)
        sample = random.choices(list(model), weights=list(model.values()), k=1)[0]
        pagerank.update({sample: pagerank[sample] + 1}) if sample in pagerank else pagerank.update({sample: 1})

    for page in corpus:
        pagerank.update({page: pagerank[page] / n}) if page in pagerank else pagerank.update({page: 0})

    return pagerank


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    pagerank = {}
    # each page rank 1/N
    N = len(corpus)
    for page in corpus: pagerank.update({page: 1/N})
    first_sum = (1 - damping_factor) / N
    convergence = False

    while not convergence:
        # count to check convergence
        count = 0
        
        for p in corpus:
            new_prob = 0
            # iterate threw pages that link to p
            for i, pages in corpus.items():
                if len(pages) == 0:
                    new_prob = new_prob + pagerank[i] / len(corpus)
                elif p in pages:
                    new_prob = new_prob + pagerank[i] / len(pages)
            new_prob = first_sum + damping_factor*new_prob

            # count for convergence check
            if abs(new_prob - pagerank[p]) < 0.001:
                count = count + 1
            pagerank[p] = new_prob

        #convergence check
        if count == N:
            convergence = True

    return pagerank

if __name__ == "__main__":
    main()
