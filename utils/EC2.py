import boto3

ec2 = None

if not ec2:
    ec2 = boto3.resource('ec2', region_name='eu-west-3')

def start_instance(parameters=None):
    ec2Instance = ec2.Instance('i-0d65edf0569acd879')
    state = ec2Instance.state['Name']
    if state == 'stopped':
        ec2Instance.start()
    elif state == 'running' and parameters is not None and 'force' in parameters and parameters['force'] == '1':
        ec2Instance.reboot()
