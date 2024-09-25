def test_from_file_to_hypergraph():
    import sys
    import os

    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
    from utils import from_file_to_hypergraph

    # fmt: off
    r"""Test the function `from_file_to_hypergraph`.
    """
    # fmt: on
    file_path = "data/test_hypergraph/test_01.hgr"
    hypergraph = from_file_to_hypergraph(file_path, True)
    assert hypergraph.num_v == 26
    assert hypergraph.num_e == 3
    print(hypergraph.e)
    print("Test passed.")

def test_from_pickle_to_hypergraph():
    import sys
    import os

    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
    from utils import from_pickle_to_hypergraph

    # fmt: off
    r"""Test the function `from_pickle_to_hypergraph`.
    """
    # fmt: on
    dataset = "test_hypergraph/H.pickle"
    hypergraph = from_pickle_to_hypergraph(dataset)
    assert hypergraph.num_v == 26
    assert hypergraph.num_e == 3
    print(hypergraph.e)
    print("Test passed.")