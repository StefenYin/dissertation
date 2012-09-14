% This file loads the paths into a structure.

f = fopen('defaults.cfg');

while 1
    line = fgetl(f);
    if ~ischar(line)
        break
    end
    if strfind(line, '=')
        if regexp(line, '%\(\w*\)s')
            line = regexprep(line, '%\((\w*)\)s', '${paths.($1)}');
        end
        pair = regexp(line, '=', 'split');
        paths.(strtrim(pair{1})) = strtrim(pair{2});
    end
end

fclose(f);

clear f line pair ans
