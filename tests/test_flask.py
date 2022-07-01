import pytest
from uh50 import create_app
from uh50.ultraheat import Uh50


@pytest.fixture()
def app():
    app = create_app(
        {
            "TESTING": True,
            "CACHE_TYPE": "SimpleCache",
        }
    )

    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture
def mock_response(monkeypatch):
    def mock_init(self, comport):
        pass

    def mock_readdata(self):
        return [
            "6.8(0203.951*GJ)6.26(02062.98*m3)9.21(00000000)",
            "6.26*01(01968.44*m3)6.8*01(0192.076*GJ)",
            "F(0)9.20(00000000)6.35(60*m)",
            "6.6(0013.0*kW)6.6*01(0013.0*kW)6.33(000.528*m3ph)9.4(082.2*C&079.6*C)",
            "6.31(0112064*h)6.32(0000339*h)9.22(R)9.6(000&00000000&0&000&00000000&0)",
            "9.7(20000)6.32*01(0000339*h)6.36(01-01&00:00)6.33*01(000.528*m3ph)",
            "6.8.1()6.8.2()6.8.3()6.8.4()6.8.5()",
            "6.8.1*01()6.8.2*01()6.8.3*01()",
            "6.8.4*01()6.8.5*01()",
            "9.4*01(082.2*C&079.6*C)",
            "6.36.1(2012-02-19)6.36.1*01(2012-02-19)",
            "6.36.2(2019-12-22)6.36.2*01(2019-12-22)",
            "6.36.3(2018-02-27)6.36.3*01(2018-02-27)",
            "6.36.4(2019-10-25)6.36.4*01(2019-10-25)",
            "6.36.5()6.36*02(01&00:00)9.36(2022-06-30&13:40:07)9.24(1.5*m3ph)",
            "9.17(0)9.18()9.19()9.25()",
            "9.1(0&1&0&0000&0000&0000&0&0.00&0.16&F&000000&000000&00&0)",
            "9.2(&&)9.29()9.31(0012747*h)",
            "9.0.1(00000000)9.0.2(00000000)9.34.1(000.00000*m3)9.34.2(000.00000*m3)",
            "8.26.1(00000000*m3)8.26.2(00000000*m3)",
            "8.26.1*01(00000000*m3)8.26.2*01(00000000*m3)",
            "6.26.1()6.26.4()6.26.5()",
            "6.26.1*01()6.26.4*01()6.26.5*01()0.0(00000000)",
        ]

    monkeypatch.setattr(Uh50, "__init__", mock_init)
    monkeypatch.setattr(Uh50, "readdata", mock_readdata)


def test_request_home_mocked(client, mock_response):
    response = client.get("/")

    assert response.status_code == 200
    assert response.json["QuantityOfHeat"] == 203.951
    assert response.json["Volume"] == 2062.98
    assert response.json["MeterDateTime"] == "Thu, 30 Jun 2022 13:40:07 GMT"


def check_app():
    app = create_app()

    assert isinstance(app, None)


def test_request_home_notfound(client):
    response = client.get("/notfound")

    assert response.status_code == 404


def test_request_home(client):
    response = client.get("/")

    assert response.status_code == 500
