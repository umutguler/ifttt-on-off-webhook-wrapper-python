"""
Implementation for ifttt_webhook to send turn on/off command.
"""
import os
from ifttt_webhook import IftttWebhook
from dotenv import load_dotenv

load_dotenv()


class IftttOnOff:
    """
    Implementation for ifttt_webhook to send turn on/off command.
    """

    def __init__(self):
        key = os.getenv("IFTTT_WEBHOOK_KEY")
        if not key:
            raise ValueError("IFTTT_WEBHOOK_KEY environment variable not set.")
        self.ifttt_webhook = IftttWebhook(key)

    def _trigger_event(self, event_name_key):
        event_name = os.getenv(event_name_key)
        if not event_name:
            raise ValueError(f"{event_name_key} environment variable not set.")
        self.ifttt_webhook.trigger(event_name)

    def turn_off(self):
        """Turns off device using the IFTTT trigger."""
        self._trigger_event("IFTTT_EVENT_OFF")

    def turn_on(self):
        """Turns on device using the IFTTT trigger."""
        self._trigger_event("IFTTT_EVENT_ON")
