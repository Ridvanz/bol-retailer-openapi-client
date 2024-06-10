# AudioTracks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disc_number** | **str** | The disc number within an album the audio track is stored on. | [optional] 
**track_number** | **str** | The track number on the album. | [optional] 
**disc_side** | **str** | The disc side on which the audio track is stored on. | [optional] 
**title** | **str** | The title of the audio track. | [optional] 
**artist_name** | **str** | The name of the artist(s) performing the audio track. | [optional] 
**play_time** | **str** | The play time of the audio track. | [optional] 
**clip_url** | **str** | The URL on which an audio clip of the audio track has been made available. | [optional] 
**clip_type** | **str** | The format in which the audio clip is available. | [optional] 

## Example

```python
from openapi_client.models.audio_tracks import AudioTracks

# TODO update the JSON string below
json = "{}"
# create an instance of AudioTracks from a JSON string
audio_tracks_instance = AudioTracks.from_json(json)
# print the JSON string representation of the object
print(AudioTracks.to_json())

# convert the object into a dict
audio_tracks_dict = audio_tracks_instance.to_dict()
# create an instance of AudioTracks from a dict
audio_tracks_from_dict = AudioTracks.from_dict(audio_tracks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


