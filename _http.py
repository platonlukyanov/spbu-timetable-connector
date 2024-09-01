import requests

def get_file_bytes_by_url(url: str, session: requests.Session):
    """
    Retrieves the content of a file from the given URL using the provided session.

    Args:
        url (str): The URL of the file to retrieve.
        session (requests.Session): The session to use for the HTTP request.

    Returns:
        bytes: The content of the file as bytes.

    """
    res = session.get(url)
    bytes_content = res.content
    session.close()
    return bytes_content
