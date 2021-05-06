#include <Python.h>
#include <stdio.h>
/**
 * print_python_list_info - print basic info python
 * @p: pointer to Python
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *list = (PyListObject *) p;
	int size, size_ = -1;

	size = ((int)Py_SIZE(p));

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", list->allocated);

	while (++size_ < size)
	{
		printf("Element %d: %s\n", size_,
		       Py_TYPE(list->ob_item[i])->tp_name);
	}
}
