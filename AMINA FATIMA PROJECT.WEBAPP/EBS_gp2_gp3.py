import boto3

def lambda_ebs(volume_arn):
    arn_parts = volume_arn.split(':')
    volume_id = arn_parts[-1].split('/')[-1]
    #volume_id = volume_arn.split('/')[1] #one time split this is written AF
    # TODO implement
    return volume_id
   
def lambda_handler(event, context):
   volume_arn = event['resources'][0]
   volume_id = lambda_ebs(volume_arn)
   
   client = boto3.client('ec2')
   
   response = client.modify_volume(
    VolumeId=volume_id,
    VolumeType='gp3',
)
