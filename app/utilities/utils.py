from collections import defaultdict


# Helper function to check for valid year (either int or digit string)
def is_valid_year(year):
    return isinstance(year, int) or (isinstance(year, str) and year.isdigit())


def group_and_sort_data_by_data_field(data):
    if not data:
        return {}

    grouped_data = defaultdict(list)

    for row in data:
        grouped_data[row["data_field"]].append(row)

    for key, rows in grouped_data.items():
        # Split rows into valid years and null/invalid years
        valid_years = [row for row in rows if row["year"] is not None and is_valid_year(row["year"])]
        null_years = [row for row in rows if row["year"] is None or not is_valid_year(row["year"])]

        # Convert valid year strings to integers
        for row in valid_years:
            if isinstance(row["year"], str) and row["year"].isdigit():
                row["year"] = int(row["year"])

        # Sort valid years by year in descending order
        if valid_years:
            valid_years.sort(key=lambda x: x["year"], reverse=True)
        
        # Combine valid years and null years back (null years remain in their original position)
        grouped_data[key] = valid_years + null_years

    return {key: value for key, value in grouped_data.items()}
