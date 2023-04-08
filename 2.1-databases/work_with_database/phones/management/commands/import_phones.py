import csv

from django.core.management.base import BaseCommand
from phones.models import Phone
from django.utils.text import slugify


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.reader(file, delimiter=';'))

        for phone in phones[1:]:
            phone = Phone(
                name = phone[1],
                image = phone[2],
                price = phone[3],
                release_date = phone[4],
                lte_exists = phone[5],
                slug = slugify(phone[1])
                )
            phone.save()
    