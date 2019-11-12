import logging

from funcy import walk_values
import click
import click_log

from .storage import Repo

click_log.basic_config()
log = logging.getLogger(__name__)

pass_repo = click.make_pass_decorator(Repo)


@click.group()
@click_log.simple_verbosity_option()
@click.option("--out-dir", required=True, help="Directory to put the output into")
@click.pass_context
def cli(ctx, out_dir):
    ctx.obj = Repo(out_dir)


@cli.command("extract")
@pass_repo
def extract(repo: Repo):
    log.info("Execute extract step")
    repo.storage.dummies = {"name": "HANS", "surname": "MAULWURF"}
    log.info("Done extracting")


@cli.command("transform")
@pass_repo
def transform(repo: Repo):
    log.info("Execute transform step")
    repo.storage.dummies = walk_values(lambda x: x.lower(), repo.storage.dummies)
    log.info("Done transforming")


@cli.command("load")
@pass_repo
def load(repo: Repo):
    log.info("Execute load step")
    print(repo.storage.dummies)
    log.info("Done loading")
