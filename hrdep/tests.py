from django.test import TestCase
from django.utils import timezone
from django.db.utils import IntegrityError
# Create your tests here.
from .models import Document, Staff, Post


class StaffViewTest(TestCase):
    # def test_create_normal_document(self):
    #     ps = Post(name='post')
    #     ps.save()
    #     st = Staff(first_name="name",
    #                middle_name="mid",
    #                last_name="last",
    #                post=ps)
    #     st.save()
    #     self.assertQuerysetEqual(Staff.objects.get(st), 200)

    def test_create_existed_document(self):
        ps = Post(name='post')
        ps.save()
        st = Staff(first_name="name",
                   middle_name="mid",
                   last_name="last",
                   post=ps)
        st.save()
        new_st = Staff(first_name=st.first_name,
                       middle_name=st.middle_name,
                       last_name=st.last_name,
                       post=st.post)
        with self.assertRaises(IntegrityError):
            new_st.save()


class StaffModelTest(TestCase):
    def test_create_with_empty_first_name(self):
        ps = Post(name='post')
        ps.save()
        st = Staff(first_name=None,
                   middle_name="mid",
                   last_name="last",
                   post=ps)
        with self.assertRaises(IntegrityError):
            st.save()

    def test_create_with_empty_middle_name(self):
        ps = Post(name='post')
        ps.save()
        st = Staff(first_name="mid",
                   middle_name=None,
                   last_name="last",
                   post=ps)
        with self.assertRaises(IntegrityError):
            st.save()

    def test_create_with_empty_last_name(self):
        ps = Post(name='post')
        ps.save()
        st = Staff(first_name="mid",
                   middle_name="mid",
                   last_name=None,
                   post=ps)
        with self.assertRaises(IntegrityError):
            st.save()


class DocumentViewTest(TestCase):
    def test_create_existed_document(self):
        ps = Post(name='post')
        ps.save()
        st = Staff(first_name="name",
                   middle_name="mid",
                   last_name="last",
                   post=ps)
        st.save()
        ex_doc = Document(staff=st,
                          document_type=1,
                          employ_date=timezone.now().date(),
                          dismiss_date=timezone.now().date(),
                          number=12132)
        ex_doc.save()
        new_doc = Document(staff=ex_doc.staff,
                           document_type=ex_doc.document_type,
                           employ_date=ex_doc.employ_date,
                           dismiss_date=ex_doc.dismiss_date,
                           number=ex_doc.number)
        with self.assertRaises(IntegrityError):
            new_doc.save()


class DocumentModelTest(TestCase):
    def test_create_with_empty_employ_date_field(self):
        ps = Post(name='post')
        ps.save()
        st = Staff(first_name="name",
                   middle_name="mid",
                   last_name="last",
                   post=ps)
        st.save()
        doc = Document(staff=st,
                       document_type=0,
                       employ_date=None,
                       dismiss_date=timezone.now().date(),
                       number=12132)

        with self.assertRaises(IntegrityError):
            doc.save()

    def test_create_with_empty_dismiss_date_field(self):
        ps = Post(name='post')
        ps.save()
        st = Staff(first_name="name",
                   middle_name="mid",
                   last_name="last",
                   post=ps)
        st.save()
        doc = Document(staff=st,
                       document_type=1,
                       employ_date=timezone.now().date(),
                       dismiss_date=None,
                       number=12132)

        with self.assertRaises(IntegrityError):
            doc.save()

    def test_create_with_empty_dismiss_date_field(self):
        ps = Post(name='post')
        ps.save()
        st = Staff(first_name="name",
                   middle_name="mid",
                   last_name="last",
                   post=ps)
        st.save()
        doc = Document(staff=st,
                       document_type=1,
                       employ_date=None,
                       dismiss_date=None,
                       number=12132)

        with self.assertRaises(IntegrityError):
            doc.save()
