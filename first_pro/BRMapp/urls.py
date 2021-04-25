import BRMapp.views as v
from django.conf.urls import url

#starting,ending of the url should be different...

urlpatterns = [
    url('view_books',v.fun_view_books),
    url('add_new_book',v.fun_add_new_book),
    url('SearchBook',v.fun_SearchBook),
    url('add',v.fun_add),                     #starting with add
    url('EditBook',v.fun_EditBook),
    url('delete_book',v.fun_delete_book),
    url('userlogin',v.fun_userlogin),
    url('userlogout',v.fun_userlogout),
    url('base_search',v.fun_basesearch),
    url('find',v.fun_find),

]