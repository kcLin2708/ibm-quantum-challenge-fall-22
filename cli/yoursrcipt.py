# import click
# import dimod

# @click.command()
# @click.option('--qubo')


# def solve_qubo(input):
#     print(input)
#     # bqm = dimod.BinaryQuadraticModel(input, 0.0, dimod.BINARY)
#     # sampleset = dimod.ExactSolver().sample(bqm)
#     # print(sampleset)


# if __name__ == '__main__':
#     solve_qubo()
import click

@click.command()
def cli():
    """Example script."""
    click.echo('Hello World!')