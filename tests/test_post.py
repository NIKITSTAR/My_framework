import pytest

from constants import VALID_EMAILS
from helpers.request_helper import email_exists_in_file
from helpers.requestcount_helper import RequestDataHelper
from routes.request import Request
from routes.request_homework import Request_count


class TestRequestPost:
    """Тесты для валидации email'ов и генерации списка email'ов по количеству."""

    @pytest.mark.parametrize('email', VALID_EMAILS)
    def test_email_valid(self, email, delete_valid_emails_file):
        """Позитивный тест: Проверяет, что валидные email'ы принимаются и записываются в файл."""
        response = Request.post(email)
        assert response == 200
        assert email_exists_in_file(email), f"Email {email} должен присутствовать в файле"

    def test_positive_valid_count(self):
        """Позитивный тест: Проверяет генерацию email'ов с корректными значениями count_email (от 3 до 10)."""
        valid_counts = range(3, 11)
        for count in valid_counts:
            emails = Request_count.post(count)
            assert isinstance(emails, list), f"Ожидается список, а получено {type(emails)} для count={count}"
            assert len(emails) == count, f"Ожидается {count} email'ов, а получено {len(emails)}"
            for email in emails:
                assert isinstance(email, str), f"Email должен быть строкой, а получено {type(email)}"
                assert "@" in email, f"Некорректный email: {email}"

    def test_negative_count_too_low(self):
        """Негативный тест: Проверяет отклонение значений count_email <= 2."""
        for count in [1, 2]:
            assert Request_count.post(count) == 404, f"Ожидается 404 для count={count}"

    def test_negative_count_too_high(self):
        """Негативный тест: Проверяет отклонение значений count_email >= 11."""
        for count in [11, 12, 20]:
            assert Request_count.post(count) == 404, f"Ожидается 404 для count={count}"

    def test_negative_invalid_type(self):
        """Негативный тест: Проверяет обработку неверных типов входного параметра count_email."""
        invalid_inputs = ["5", 5.0, None, [5], {}]
        for invalid in invalid_inputs:
            assert Request_count.post(invalid) == 404, f"Ожидается 404 для input={invalid}"

    def test_valid_payload_with_helper(self):
        """Позитивный тест: Использует helper для генерации корректных данных."""
        payload = RequestDataHelper.valid_payload()
        emails = Request_count.post(payload["count_email"], payload["url"])
        assert isinstance(emails, list), f"Ожидается список, а получено {type(emails)}"
        assert len(emails) == payload["count_email"], (
            f"Ожидается {payload['count_email']} email'ов, а получено {len(emails)}"
        )
        for email in emails:
            assert isinstance(email, str), f"Email должен быть строкой, а получено {type(email)}"
            assert "@" in email, f"Некорректный email: {email}"

    def test_invalid_payload_with_helper(self):
        """Негативный тест: Использует helper для генерации некорректных данных."""
        payload = RequestDataHelper.invalid_payload()
        result = Request_count.post(payload["count_email"], payload["url"])
        assert result == 404, f"Ожидается 404 для данных: {payload}"
