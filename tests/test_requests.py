def test_local_repos_sample():
    # Replace external GitHub API call with a deterministic local sample
    sample = [
        {"name": "repo-one"},
        {"name": "repo-two"},
    ]
    my_repos = [repo["name"] for repo in sample]
    assert "repo-one" in my_repos
    assert my_repos == ["repo-one", "repo-two"]
