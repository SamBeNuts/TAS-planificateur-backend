import boto3

ec2 = boto3.resource('ec2', region_name='eu-west-3')
instance = ec2.Instance('i-0d65edf0569acd879')

def start_instance():
    if instance.state['Name'] == 'stopped':
        instance.start()
