import pytest
from .subscribers_repository import SubscribersRepository

@pytest.mark.skip("Insert subscriber in DB")
def test_insert():
    subscriber_info = {
        "name": "meuNome222",
        "email": "email@email2.com",
        "evento_id": 2
    }

    subs_repo = SubscribersRepository()

    subs_repo.insert(subscriber_infos=subscriber_info)

@pytest.mark.skip("Select subscriber in DB")
def test_select_subscriber():
    email = "email@email.com"
    evento_id = 2

    subs_repo = SubscribersRepository()
    resp = subs_repo.select_subscriber(email, evento_id)

    print(resp.nome)

@pytest.mark.skip("Ranking in DB")
def test_ranking():
    event_id = 3
    subs_repo = SubscribersRepository()

    resp = subs_repo.get_ranking(event_id)

    for elem in resp:
        print(f"Link: {elem.link}, total de inscritos: {elem.total}")