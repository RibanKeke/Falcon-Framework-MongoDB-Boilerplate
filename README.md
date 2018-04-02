Falcon framework: MongoDB Boilerplate
-------------------------------------
I was looking for good falcon boilerplate for my side-project, didn't find
a satisfactory one with MongoDB already set.
I forked and inspired from the boilerplate: https://github.com/admiralobvious/falcon-boilerplate

I added the following packages:
-- MongoDB with mongoengine: http://mongoengine.org/
-- Webargs for validating the json input: https://webargs.readthedocs.io/en/latest/#
-- Unit-testing with pytest: https://docs.pytest.org/en/latest/

Already setup with a dockerfile and a compose file with the latest MongoDB container.
Build:
-----
docker-compose build

Run containers:
---------------
docker-compose up

Route:
------------
http://localhost:5000/users