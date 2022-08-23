from unittest import TestCase

from qiita_given_when_then.status import Status
from qiita_given_when_then.task import Task


class TestCreate(TestCase):

    def test_引数にタスク名を指定して新規作成することができる(self) -> None:
        # when:
        task = Task.create("テスト")

        # then:
        self.assertEqual("テスト", task.name)

    def test_引数に指定されたタスク名がNoneの場合は例外がスローされる(self) -> None:
        # when/then:
        with self.assertRaises(ValueError):
            Task.create(None)

    def test_新規作成時のステータスはOpenになる(self) -> None:
        # when:
        task = Task.create("テスト")

        # then:
        self.assertEqual(Status.Open, task.status)


class TestNextStatus(TestCase):

    def test_ステータスがOpenの状態でステータスを進めるとConfirmになる(self) -> None:
        # given:
        # タスクを新規作成する
        task = Task.create("テスト")

        # when:
        task.next_status()

        # then:
        self.assertEqual(Status.Confirm, task.status)

    def test_ステータスがConfirmの状態でステータスを進めるとInprogressになる(self) -> None:
        # given:
        # タスクを新規作成してステータスをConfirmまで進める
        task = Task.create("テスト")
        task.next_status()

        # when:
        task.next_status()

        # then:
        self.assertEqual(Status.Inprogress, task.status)

    def test_ステータスがInprogressの状態でステータスを進めるとResolveになる(self) -> None:
        # given:
        # タスクを新規作成してステータスをInprogressまで進める
        task = Task.create("テスト")
        task.next_status()
        task.next_status()

        # when:
        task.next_status()

        # then:
        self.assertEqual(Status.Resolve, task.status)

    def test_ステータスがResolveの状態でステータスを進めるとCloseになる(self) -> None:
        # given:
        # タスクを新規作成してステータスをResolveまで進める
        task = Task.create("テスト")
        task.next_status()
        task.next_status()
        task.next_status()

        # when:
        task.next_status()

        # then:
        self.assertEqual(Status.Close, task.status)

    def test_ステータスがCloseの状態でステータスを進めると例外がスローされる(self) -> None:
        # given:
        # タスクを新規作成してステータスをCloseまで進める
        task = Task.create("テスト")
        task.next_status()
        task.next_status()
        task.next_status()
        task.next_status()

        # when/then:
        with self.assertRaises(Exception):
            task.next_status()
