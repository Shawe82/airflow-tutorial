import logging
import string
import random

from funcy import walk_values, isa
import click
import click_log

from .storage import Repo

click_log.basic_config()
log = logging.getLogger(__name__)

pass_repo = click.make_pass_decorator(Repo)


def random_string(length):
    return "".join(
        random.choices(string.ascii_uppercase + string.ascii_lowercase, k=length)
    )


@click.group()
@click_log.simple_verbosity_option()
@click.option("--out-dir", required=True, help="Directory to put the output into")
@click.pass_context
def cli(ctx, out_dir):
    ctx.obj = Repo(out_dir)


@cli.command("extract")
@pass_repo
@click.option("--url", required=True, help="Url to extract the data from")
def extract(repo: Repo, url):
    log.info(f"Execute extract step from {url}")
    repo.storage.dummies = {
        random_string(8): random_string(12) for _ in range(random.randint(3, 10))
    }
    log.info("Done extracting")


@cli.command("transform")
@pass_repo
@click.option(
    "--lower",
    "action",
    default=True,
    help="Transform string to lower case",
    flag_value="lower",
)
@click.option(
    "--upper", "action", help="Transform string to upper case", flag_value="upper"
)
def transform(repo: Repo, action):
    def trans(x: str):
        if not isa(str)(x):
            return x
        return x.lower() if action == "lower" else x.upper()

    log.info("Execute transform step")
    repo.storage.dummies = walk_values(trans, repo.storage.dummies)
    log.info("Done transforming")


@cli.command("load")
@pass_repo
@click.option("--db", required=True, help="database to upload the result")
def load(repo: Repo, db):
    log.info(f"Execute load step to db {db}")
    print(repo.storage.dummies)
    log.info("Done loading")
