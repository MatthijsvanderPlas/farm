# farm

[![Run Tests](https://github.com/MatthijsvanderPlas/farm/actions/workflows/run-tests.yaml/badge.svg)](https://github.com/MatthijsvanderPlas/farm/actions/workflows/run-tests.yaml)

## CI/CD final assignment

### Three components:

- Github Actions through the `.yaml` file
- SSH connection
- Bash Script

The pipeline is pretty basic to be fair. With the Github Actions we run two jobs from a single script. By dividing the steps into two different jobs and having the second job `needs: <first job>` it now depends on the outcome of the pytest that runs at the end of the first job. If the test fail the second job will not run and thus the VPS does not update itself to the recent code changes.

SSH connection is made in the second job and thus depends on the outcome of the pytest. Here we use the sshpass and ssh in union to login to our remote VPS and execute a bash script.

The Bash script runs on the remote VPS and makes a pull request on the repository. After the pull request it restarts the gunicon service so the changes in the files are picked up on and shown.


### Three problems:

- Working ssh connection on Github Actions
- Depency on the result of the pytest
- Updating the server

I had trouble with setting up the ssh connection the right way. This still is not really the best way I think but no password or host is revealed in the workflow thanks to the secrets context. I kept getting error codes when I tried to implement it myself and pulled in someone's premade Action to take over. The problem there was that in my opinion it took a long time and a ton of installing before it ran and later gave a problem when I split into two different jobs. But if someone else was able to do it, then my secrets must be working and it is possible to get it right. Testing on my local machine if I could get it working made sure that my command should be working. Then I got the exit code: 6 which I googled and by adding an extra argument I was able to circumvent the problem(problem stems because the Github Actions always runs it for a first time which is different).

Initially I thought to have a single job and have one step depend on a previous one. In searching and googling I found that if you are using different jobs you can easily have one job depend on the other and thus solved my issues quite easily. If pytest fails the server wont update.

Updating the server itself and especially having gunicorn notice the change took a little figuring out. I decided to setup the server to simply be able to do a pull request with ssh authentication and have a simple bash script run the pull request and restart the service.

### CI/CD

I feel it is more of an DevOps type of assignment but as I will start working for a company that works with azure and C# where the pipelines are done with Github Actions I liked getting a first look at it. I did not enjoy having to use digital ocean. All in all I am happy to have come to the end of the back-end course. I do feel I at least have seen a bit of everything.