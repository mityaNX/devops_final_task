def test_index_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Random Cat Generator" in response.data


def test_like_cat(client):
    response = client.post("/like", data={
        "cat_image_url": "https://example.com/cat.jpg"
    }, follow_redirects=True)

    assert response.status_code == 200
