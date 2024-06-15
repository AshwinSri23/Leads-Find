
#! Currently not being used - Attempting with Selenium

import click
from DEPRECATEDmain import sb_rr_get_people_by_keywords, sb_rr_get_account_info

@click.command()
def test():
    print(sb_rr_get_account_info())
    click.echo("Testing...")

if __name__ == '__main__':
    test()
