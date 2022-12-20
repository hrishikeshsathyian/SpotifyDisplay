##  scopes needed
##  user-read-currently-playing
##  user-read-private
##  redirect uri --> https://www.google.com.sg/
##  Client ID ea2c27e008964e349dabb8b0b0d03acf:396f4e0404754e9caf7f03f459d8307a
##  Client Secret 396f4e0404754e9caf7f03f459d8307a
## authorization_code
## access token

spotify_user_id = "hrishikeshsathyian2002"
access_token="BQAzStOXXRTBwhIWLUvQ1dRfBBOdopWXpRG-V839WYizWVGd1hy_GuuPp7Y5xCpnd-KgxFp2SpD77_BAQKtuYg16rRxeTnEwkqf8-nSRZEWsqs7CkyT0OrnZQc0047MQBYNXrSQQnZ1iU9CLJjQ3AiuIBJj7-G7CInz3fmREGRhQbpOv5A"
refresh_token = "AQD9pqGWuDlQk66uqRhkhe6YNHCZsaRRkgk6f6F5zIYnhd5YwO6j1jL9foqzjo8r6FGqYov6iFjlNsy0xvxKf1JDCrVKCLSuIeg_i7sz_HU4wYGY1jyGmSz031wjc6K5KUo"
base_64 = "ZWEyYzI3ZTAwODk2NGUzNDlkYWJiOGIwYjBkMDNhY2Y6Mzk2ZjRlMDQwNDc1NGU5Y2FmN2YwM2Y0NTlkODMwN2E="

# https://accounts.spotify.com/authorize?client_id=ea2c27e008964e349dabb8b0b0d03acf&response_type=code&redirect_uri=https%3A%2F%2Fwww.google.com%2F&scope=user-read-currently-playing%20user-read-private

# https://www.google.com/?code=AQAOMBYHH_xbY2_ZWN3PUJEWcZaYJ0fSwu8dQ2EJ1WOFWeen6__wtL_7EIOphqJ_QhACzRhAw2bgLQ40EXSWQYDSrYpyT-m8NO_SWKcwXxdOTC61Wbt0a9Xyfq_PHDpYqPiDqkp1Dw-ctgj659S_a4xqkhat8AmVxQeWbyz3eoqiI73vUD5G_SxsspI4NjSSHGObM_jEnuRk01L-5alQFDXS5hRI0hLuho-g


#
#
# curl -H "Authorization: Basic ZWEyYzI3ZTAwODk2NGUzNDlkYWJiOGIwYjBkMDNhY2Y6Mzk2ZjRlMDQwNDc1NGU5Y2FmN2YwM2Y0NTlkODMwN2E=" -d grant_type="authorization_code" -d code=AQArYmlOg3k16jxZpOVCQ3JAZNgtnDwvtQMst_5uB4LkEGTJ9tEqQfO56Z7SFgJE6Wiwh96SbARlpkuCUQqFjB2O_RLSRYj8j986sMhgRWQyqHPzb3YJgV9iEXTaIM6inlEgyZ1wy3g6U8frcLeFd3hxW8XW49gnddkoeWvm2w7DdYzPNFfZ1Dvghy71MxWQ_SxKau9MApy_izpEi-aAYTkpqIqTg_laoWAO -d redirect_uri=https%3A%2F%2Fwww.google.com%2F https://accounts.spotify.com/api/token
# {"access_token":"BQAzStOXXRTBwhIWLUvQ1dRfBBOdopWXpRG-V839WYizWVGd1hy_GuuPp7Y5xCpnd-KgxFp2SpD77_BAQKtuYg16rRxeTnEwkqf8-nSRZEWsqs7CkyT0OrnZQc0047MQBYNXrSQQnZ1iU9CLJjQ3AiuIBJj7-G7CInz3fmREGRhQbpOv5A","token_type":"Bearer","expires_in":3600,"refresh_token":"AQD9pqGWuDlQk66uqRhkhe6YNHCZsaRRkgk6f6F5zIYnhd5YwO6j1jL9foqzjo8r6FGqYov6iFjlNsy0xvxKf1JDCrVKCLSuIeg_i7sz_HU4wYGY1jyGmSz031wjc6K5KUo","scope":"user-read-currently-playing user-read-private"}
