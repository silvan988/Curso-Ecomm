def formata_preco(val):
    # return f'R$ {val:,.2f}'.replace('.', ',')
    try:
        import locale
        valor_int = float(val)
        locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')
        val = locale.currency(valor_int, grouping=True)
        return val
    except ValueError:
        # Trate o erro
        raise
