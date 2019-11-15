import logging
import string
import random

from funcy import walk_values, isa
import click
import click_log

from .storage import Storage

click_log.basic_config()
log = logging.getLogger(__name__)

pass_storage = click.make_pass_decorator(Storage)


def random_string(length):
    return "".join(
        random.choices(string.ascii_uppercase + string.ascii_lowercase, k=length)
    )


@click.group()
@click_log.simple_verbosity_option()
@click.option("--redis-url", required=True, help="Redis connection URL")
@click.pass_context
def cli(ctx, redis_url):
    ctx.obj = Storage(redis_url)


@cli.command("extract")
@pass_storage
@click.option("--url", required=True, help="Url to extract the data from")
def extract(repo: Storage, url):
    log.info(f"Execute extract step from {url}")
    repo.dummies = {
        random_string(8): random_string(12) for _ in range(random.randint(3, 10))
    }
    log.info("Done extracting")


@cli.command("transform")
@pass_storage
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
def transform(repo: Storage, action):
    def trans(x: str):
        if not isa(str)(x):
            return x
        return x.lower() if action == "lower" else x.upper()

    log.info("Execute transform step")
    repo.dummies = walk_values(trans, repo.dummies)
    log.info("Done transforming")


@cli.command("load")
@pass_storage
@click.option("--db", required=True, help="database to upload the result")
def load(repo: Storage, db):
    log.info(f"Execute load step to db {db}")
    print(repo.dummies)
    log.info("Done loading")
