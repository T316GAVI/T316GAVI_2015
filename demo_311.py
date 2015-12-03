import pandas as pd
import matplotlib.pyplot as plt

complaints = pd.read_csv('311-service-requests.csv')

#print(complaints.dtypes)


#print(complaints['Complaint Type'])


#print(complaints['Complaint Type'][:5])

#print(complaints[['Complaint Type', 'Borough']][:10])

#print(complaints['Complaint Type'].value_counts())


#common_complaints = complaints['Complaint Type'].value_counts()

#print(common_complaints[:10])

#common_complaints[:10].plot(kind='bar', figsize=(15,5))
#plt.show()

#noise_complaints = complaints[complaints['Complaint Type'] == "Noise - Street/Sidewalk"]

#print(noise_complaints)


#is_noise = complaints['Complaint Type'] == "Noise - Street/Sidewalk"
#in_brooklyn = complaints['Borough'] == "BROOKLYN"

#print(complaints[is_noise & in_brooklyn][:5])

#print(complaints[is_noise & in_brooklyn][['Complaint Type', 'Borough', 'Created Date', 'Descriptor']][:10])

is_noise = complaints['Complaint Type'] == "Noise - Street/Sidewalk"
noise_complaints = complaints[is_noise]
print(noise_complaints['Borough'].value_counts())

noise_complaint_counts = noise_complaints['Borough'].value_counts()
complaint_counts = complaints['Borough'].value_counts()

print(noise_complaint_counts / complaint_counts)
(noise_complaint_counts / complaint_counts).plot(kind='bar')
plt.show()

