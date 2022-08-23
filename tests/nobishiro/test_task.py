from unittest import TestCase

from qiita_given_when_then.status import Status
from qiita_given_when_then.task import Task


class TestNextStatus(TestCase):

    def test_ステータスがResolveの状態でステータスを進めるとCloseになる(self) -> None:
        task = Task.create("テスト")
        task.next_status()
        task.next_status()
        task.next_status()
        task.next_status()

        self.assertEqual(Status.Close, task.status)

    def test_ステータスがCloseの状態でステータスを進めると例外がスローされる(self) -> None:
        task = Task.create("テスト")
        task.next_status()
        task.next_status()
        task.next_status()
        task.next_status()

        with self.assertRaises(Exception):
            task.next_status()
