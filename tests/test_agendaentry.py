from lib.agendaentry import AgendaEntry

def test_agenda_entry():
    entry = AgendaEntry("my title", "my contents")
    assert entry.title == "my title"
    assert entry.contents == "my contents"