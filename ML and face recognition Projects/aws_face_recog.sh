#!/bin/bash

#Take a photo using RPI camera
echo "Taking picture !!"
raspistill -o capturedpic.jpg

#Upload the photo to the S3 bucket
echo "Uploading and Analyzing.. Please wait !!"
aws s3 cp capturedpic.jpg s3://team1-bnmit
sleep 5

picName="capturedpic.jpg"

#Declare a variable to store the image and bucket info to use in search faces command
foo=$(cat <<EOF
{
"S3Object":{
"Bucket":"team1-bnmit",
"Name":"$picName"
}
}
EOF
)

member1="306acf81-2085-4906-9f2d-2342c4c31777"
member2="sdfsdf-2085-4906-9f2d-sdfsfsdf"

#Search for faces
Face_id=$(aws rekognition search-faces-by-image --image "$foo" --collection-id "team1" --region ap-south-1 --profile default| jq '.FaceMatches| .[] | .Face.FaceId')
echo $Face_id

#Remove extra things and extract only face id
faceid_formatted=$(echo "$Face_id" | sed -e 's/^"//' -e 's/"$//')
echo $faceid_formatted

#Function to send an email
send_mail () {
  aws ses send-email --from "abc@gmail.com" --destination "ToAddresses=abc@gmail.com" --message "Subject={Data=from recognition system,Charset=utf8},Body={Text={Data=$1,Charset=utf8},Html={Data=$1,Charset=utf8}}"
}

#Check if the person belongs to your team or not and send mail accordingly
if [ -z $faceid_formatted ]
then
    echo "No human face found"
	send_mail NoHumanFaceFound
elif [ $faceid_formatted = $member1 ]
then
    echo "Hai Sandeep, Welcome"
    send_mail Sandeep
elif [ $faceid_formatted = $member2 ]
then
    echo "Hai Rama, Welcome"
    send_mail Rama
else
    echo "Not a team member"
    send_mail UnauthorizedPerson
fi
