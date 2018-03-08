# ------------------------------------------------------------------------------
#
# ----------------
# TERMINAL MODS
# ----------------
#
alias ..='cd ../'                   # Go back 1 directory level
alias ls='ls -G'                    # Add color to list output
alias ll='ls -Flah'                 # Detailed long list
alias cp='cp -iv'                   # Safer overwrite copy
alias mv='mv -iv'                   # Safer overwrite move
alias ln='ln -iv'                   # Safer overwrite link
alias edit='atom'                   # Open file in Atom
alias find='open -a Finder ./'      # Open dir in Finder
alias prev='open -a Preview ./'     # Open file in Preview

# ----------------
# COMMAND PROMPT
# ----------------

fill="___ "
reset_style='\[\033[00m\]'
status_style=$reset_style'\[\033[0;90m\]' # 0;90 for gray; use 0;37m for lighter
prompt_style=$reset_style
command_style=$reset_style'\[\033[1;29m\]' # bold black

PS1="$status_style"'$fill \t\n'"$prompt_style"'${debian_chroot:+($debian_chroot)}\u@\h:\w $'"$command_style "

trap 'echo -ne "\033[00m"' DEBUG

function prompt_command {

let fillsize=${COLUMNS}-9
fill=""
while [ "$fillsize" -gt "0" ]
do
fill="-${fill}"
let fillsize=${fillsize}-1
done

case "$TERM" in
xterm*|rxvt*)
bname=`basename "${PWD/$HOME/~}"`
echo -ne "\033]0;${bname}: ${USER}@${HOSTNAME}: ${PWD/$HOME/~}\007"
;;
*)
;;
esac
}

PROMPT_COMMAND=prompt_command

# Setting PATH for Python 3.6
# The original version is saved in .bash_profile.pysave
PATH="/Library/Frameworks/Python.framework/Versions/3.6/bin:${PATH}"
export PATH

# added by Anaconda3 5.0.0 installer
export PATH="/Users/james/anaconda3/bin:$PATH"

# added by Anaconda3 5.0.1 installer
export PATH="/Applications/anaconda3/bin:$PATH"
