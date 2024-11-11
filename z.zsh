

config_configure() {
    session=$(python3 cli.py session_new)
    echo "SESSION: $session"
    if [ $? -ne 0 ]; then
	echo "Error creating session"
        return 1
    fi
    export CONFIG_SESSION=$session
    export CONFIG_EDIT_LEVEL=''
}


config_show() {
    if [ -z "${CONFIG_SESSION}" ]; then
        echo "show, Please start session first"
	return 1
    fi
    python3 cli.py config_show "$@"
}

config_set() {
    if [ -z "${CONFIG_SESSION}" ]; then
        echo "set, Please start session first"
	return 1
    fi
    python3 cli.py config_set "$@"
}

config_delete() {
    if [ -z "${CONFIG_SESSION}" ]; then
        echo "delete, Please start session first"
	return 1
    fi
    python3 cli.py config_del "$@"
}

override_zsh_qmark() {
    printf '\n'
    python3 cli.py compline "$BUFFER"
    zle reset-prompt
}
zle -N override_zsh_qmark
bindkey "?" override_zsh_qmark

_config_set_completion() {
    COMPREPLY=($(compgen -W "$(python3 cli.py comp_set ${COMP_WORDS[@]})" -- "${COMP_WORDS[1]}"))
}

alias configure=config_configure
alias show=config_show
alias set=config_set
alias del=config_delete

#complete -F _config_set_completion set
#exit() {
#    echo "bump"
#}
