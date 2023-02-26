import datetime

import pytest

from forms_app.forms import ContactForm


@pytest.mark.parametrize(
    "date_creation, subject, message, sender, cc_myself, validity",
    [
        # Fully correct data
        (datetime.date.today(), "Subject", "Message", "random82@mail.ru", True, True),
        # Date creastion is in the past
        ("2000-00-01", "Subject", "Message", "random82@mail.ru", True, False),
        # Email has incorrect format
        ("2000-00-01", "Subject", "Message", "random82mail.ru", True, False),
    ],
)
def test(date_creation, subject, message, sender, cc_myself, validity):
    data = {
        "date_creation": date_creation,
        "subject": subject,
        "message": message,
        "sender": sender,
        "cc_myself": cc_myself,
    }
    form = ContactForm(data)

    assert form.is_valid() is validity
