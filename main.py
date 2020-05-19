#!/usr/bin/env python
# -*- coding: utf-8 -*-

SYSTEM_META_FILE_PATH = 'sys/tables_files_meta.csv'

def main():
    tables_files = []

    def init():
    """Initial processing before all.

    Args:
        None

    Returns:
        None
    """
        def _read_system_meta(system_meta_file_path):
        """Read the specified file for loading a map of

        Args:
            system_meta_file_path (str):
                a file path which is written a map of tables and data files
        Return:
            tables_files:
                a tupple which is letting us know a file path for an arbitrary table.

        """
            with open(system_meta_file_path) as f:
                lines = f.readlines()

            tables_files = [tuple(line.strip().split(',')) for line in lines]

            return tables_files

        tables_files = _read_system_meta(SYSTEM_META_FILE_PATH)

    def query_prompt():
        """Prompto for query which is input by client.
        When input query string is invalid in grammer,this shows usage
        description.

        Extended description of function.

        Args:
             None

        Returns:
             sql_queries: If all sql sentences are valid, return tuple of sql queries.
                          If any invalid sql are input, return None

        """

        def usage():
            """Show an usage document.

            Args:
                None

            Returns:
                0

            """
            print('Usage: SELECT <columns separated by comma> FROM <table name>')
            return

        def check_validation(query_string):
            """Check grammer for inpute sql query.

            Args:
                query_string (str): an input string of a query

            Retruns:
                (code, message): if any incorrect grammer as sql, code should be 1
                                 and a error message which show in detail.
                                 If not, code is 0 and message is None.
            """
            query_terms = query_string.strip().split(' ')

            # check first term is permitted.
            if query_terms[0].lower() != 'select':
                return (1, 'Input string is invalid. Not start with "SELECT"')

            return (0,None)

        query_string = input('Input:')
        sql_queries = query_string.split(';')

        for sql_query in sql_queries:
            ret = check_validation(sql_query)
            if ret[0]:
                print(ret[1])
                usage()
            return None

        return sql_queries

    def query_parser(sql_query):
        terms = sql_query.strip().split(' ')

        type = terms[0].lower()
        colmns = terms[1].split(',')
        table = terms[3].lower()
        filters = terms[5].lower().split(' AND ')

    # Wait for input query string
    while:
        ret_queryprompt = query_prompt()
        if ret_qureyprompt:
            continue

        for sql_query in ret_queryprompt:
            ret_queryparser = query_parser(sql_query)



if __name__ == '__main__':
    main()
