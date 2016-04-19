import json
import sys
import click
from kong.api import API
from kong.decorators import verify_config

@click.group()
@click.pass_context
@verify_config
def cli(ctx):
    if ctx.obj is None:
        ctx.obj = {}


@cli.command()
@click.option('--add', 'action', flag_value='add')
@click.option('--name', '-n', 'name', default=None)
@click.option('--upstream', '-u', 'upstream', default=None)
@click.option('--host', '-h', 'host', default=None)
@click.pass_context
def apis(ctx, action, name, upstream, host):
    client = API(ctx.obj['base_url'])

    if not action:
        print_json(client.get_api_endpoints())
    else:
        if filter(lambda x: x is None, [name, upstream, host]):
            click.echo('You must supply: name, upstream & host parameters')
            sys.exit(1)

        if action == 'add':
            click.echo('Adding')


@cli.command()
@click.pass_context
def consumers(ctx):
    client = API(ctx.obj['base_url'])

    print_json(client.get_consumer_endpoints())


def print_json(data):
    click.echo(json.dumps(data, sort_keys=True, indent=4, separators=(',', ': ')))

if __name__ == "__main__":
    cli(obj={})
