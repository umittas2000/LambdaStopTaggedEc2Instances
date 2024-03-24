import boto3
def stop_tagged_ec2instances(ec2,filters,region_):
    #Scope resources to instances with given tag filters
    instances = ec2.instances.filter(Filters=filters)

    #iterate collected instances and stop them
    for instance in instances:
        #instance.stop()
        data.append("Region: "+ region_+ " | Stopped Instance: "+instance.id+ " | Tags: "+ str(instance.tags))

if __name__ == '__main__':
    data = []

    #Create a filter to catch ec2 running instances with given tags
    filters = [
        {'Name': 'instance-state-name', 'Values': ['running']},
        {'Name': 'tag:resources', 'Values': ['my-stack']}
    ]

    #Define the regions where we will look at running ec2 instances
    regions = ['us-east-1', 'us-east-2', 'ca-central-1']


    for region_ in regions:
        # Set the region you would like to stop instances
        client = boto3.setup_default_session(region_name=region_)

        # scope resources to ec2
        ec2 = boto3.resource('ec2')

        #Call the method with necessary parameter
        stop_tagged_ec2instances(ec2,filters,region_)
    print(data)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
