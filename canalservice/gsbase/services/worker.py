
import time
from .utils import get_json_data


def сompletely_update_db(model):
    while True:
        new_data = get_json_data()
        model.objects.all().delete()
        for order in new_data:
            model.objects.create(**order)
        time.sleep(10)
        return True
