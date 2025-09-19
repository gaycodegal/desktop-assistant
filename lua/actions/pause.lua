--[[pause playing of current song
   ;; pause -> pause current audio
   https://developer.android.com/reference/android/support/v4/media/session/PlaybackStateCompat#ACTION_PAUSE()
]]
function main()
    jcall("sendMediaButtonAction", 2)
    jcall("quit")
    return "ok"
end
