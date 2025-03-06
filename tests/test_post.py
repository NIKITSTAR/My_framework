import pytest

from constants import VALID_EMAILS
from helpers.request_helper import email_exists_in_file
from helpers.requestcount_helper import RequestDataHelper
from routes.request import request
from routes.request_homework import Request_count


class TestRequestPost:

    @pytest.mark.parametrize('email', VALID_EMAILS)
    def test_email_valid(self, email, delete_vaild_emails_file):
        response = request.post(email)
        assert response == 200
        assert email_exists_in_file(email)

    """Позитивный тест: корректное значение count_email"""
    def test_positive_valid_count(self):
        valid_counts = [3, 4, 5, 6, 7, 8, 9, 10]
        for count in valid_counts:
            emails = Request_count.post(count)
            assert isinstance(emails, list), f"Ожидается список, а получено {type(emails)} для count={count}"
            assert len(emails) == count, f"Ожидается {count} email, а получено {len(emails)}"
            for email in emails:
                assert isinstance(email, str), f"Email должен быть строкой, а получено {type(email)}"
                assert "@" in email, f"Некорректный email: {email}"

    """Негативный тест: count_email меньше или равно 2"""
    def test_negative_count_too_low(self):
        for count in [1, 2]:
            assert Request_count.post(count) == 404, f"Ожидается 404 для count={count}"

    """Негативный тест: count_email больше или равно 11"""
    def test_negative_count_too_high(self):
        for count in [11, 12, 20]:
            assert Request_count.post(count) == 404, f"Ожидается 404 для count={count}"

    """Негативный тест: неверный тип входного параметра"""
    def test_negative_invalid_type(self):
        invalid_inputs = ["5", 5.0, None, [5], {}]
        for invalid in invalid_inputs:
            assert Request_count.post(invalid) == 404, f"Ожидается 404 для input={invalid}"

    """Позитивный тест с использованием helper: корректные данные"""
    def test_valid_payload_with_helper(self):
        payload = RequestDataHelper.valid_payload()
        emails = Request_count.post(payload["count_email"], payload["url"])
        assert isinstance(emails, list), f"Ожидается список, а получено {type(emails)}"
        assert len(emails) == payload["count_email"], (
            f"Ожидается {payload['count_email']} email, а получено {len(emails)}"
        )
        for email in emails:
            assert isinstance(email, str), f"Email должен быть строкой, а получено {type(email)}"
            assert "@" in email, f"Некорректный email: {email}"

    """Негативный тест с использованием helper: некорректные данные"""
    def test_invalid_payload_with_helper(self):
        payload = RequestDataHelper.invalid_payload()
        result = Request_count.post(payload["count_email"], payload["url"])
        assert result == 404, f"Ожидается 404 для данных: {payload}"
