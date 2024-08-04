source carla-env/bin/activate 
cd carla && ./CarlaUE4.sh
cd carla/PythonAPI/examples && python generate_traffic.py
cd carla/PythonAPI/examples && python manual_control.py
cd carla/carla_project && code .
cd scenario_runner-0.9.15
python scenario_runner.py --scenario FollowLeadingVehicle_1 --reloadWorld
cd scenario_runner-0.9.15 && python manual_control.py
cd scenario_runner-0.9.15


export CARLA_ROOT=/home/sumaiya/carla/PythonAPI/carla/agents
export CARLA_ROOT=/home/sumaiya/carla/PythonAPI/carla/dist
export SCENARIO_RUNNER_ROOT=/home/sumaiya/scenario_runner-0.9.15
export PYTHONPATH=/usr/local/bin/python:/home/sumaiya/carla/PythonAPI/carla/dist/carla-0.9.15-py3.7-linux-x86_64.egg
export PYTHONPATH=/usr/local/bin/python:/home/sumaiya/carla/PythonAPI/carla

0. Start Carla
1. Start DB
2. Start API server
3. Run client