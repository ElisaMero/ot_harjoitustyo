

from invoke import task


@task
def start(ctx):
    ctx.run("python3 src/mainplatform.py", pty=True)



@task
def test(ctx):
    ctx.run("coverage run --branch -m pytest src", pty=True)


@task(test)
def coverage_report(ctx):
    ctx.run("coverage html", pty=True)