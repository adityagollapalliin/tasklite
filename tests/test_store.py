from tasklite.store import TaskStore


def make_store(tmp_path):
    return TaskStore(tmp_path / "tasks.json")


def test_add_and_reload(tmp_path):
    store = make_store(tmp_path)
    store.add("Buy milk")
    reloaded = make_store(tmp_path)
    assert [t.title for t in reloaded.tasks] == ["Buy milk"]


def test_complete(tmp_path):
    store = make_store(tmp_path)
    task = store.add("Write report")
    store.complete(task.id)
    assert store.get(task.id).done is True


def test_remove(tmp_path):
    store = make_store(tmp_path)
    task = store.add("Call Bob")
    store.remove(task.id)
    assert store.tasks == []
