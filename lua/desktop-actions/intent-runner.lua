json = require("third_party/json")

function jcall(...)
   local arg={...}
   print(json.encode(arg))
end


function run_intent(arg_string)
   local arguments = {}
   for argument in arg_string:gmatch("%S+") do table.insert(arguments, argument) end
   local command = arguments[1]
   require("lua/actions/"..command)
   --print(table.concat(arguments, " "))
   jcall("result", main(arguments))
end

run_intent(arg[1])
