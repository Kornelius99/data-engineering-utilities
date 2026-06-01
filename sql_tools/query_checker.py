def check_select_star(query: str) -> bool:
    """
    Detect SELECT * usage.
    """
    return "select *" in query.lower()


def check_missing_where(query: str) -> bool:
    """
    Detect queries without WHERE clause.
    """
    return "where" not in query.lower()


def basic_sql_review(query: str) -> dict:
    """
    Run basic SQL review checks.
    """
    return {
        "uses_select_star": check_select_star(query),
        "missing_where_clause": check_missing_where(query),
    }


if __name__ == "__main__":
    sample_query = "SELECT * FROM sales"

    review = basic_sql_review(sample_query)

    print(review)