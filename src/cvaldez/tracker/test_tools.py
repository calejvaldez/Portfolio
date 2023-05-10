import unittest
from tools import create_project
import psycopg2
import os


class MyTestCase(unittest.TestCase):
    def test_project_creation(self):
        p = create_project('Test', 'This is a test project')

        try:
            self.assertEqual((p.name, p.description, p.version, p.link, p.icon, p.status),
                             ('Test', 'This is a test project', None, None, 'building.svg', '1'))
        finally:
            with psycopg2.connect(os.getenv("DB_LINK")) as con:
                cur = con.cursor()
                cur.execute("DELETE FROM pst_projects WHERE id=%s", (p.id,))

                cur.execute("SELECT * FROM pst_projects WHERE id=%s", (p.id,))

                self.assertEqual(len(cur.fetchall()), 0)


if __name__ == '__main__':
    unittest.main()
