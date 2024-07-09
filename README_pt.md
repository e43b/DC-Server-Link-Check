# DC Server Link Check

[![Donate](https://img.shields.io/badge/Donate-Oxapay-blue)](https://oxapay.com/donate/40874860)
[![Discord](https://img.shields.io/badge/Discord-Join%20Server-blue)](https://discord.gg/CsBMMXBz7t)

**GitHub Project**: [DC Server Link Check](https://github.com/e43b/DC-Server-Link-Check/)
**Author**: [e43b](https://github.com/e43b)

## Descrição

O projeto **DC Server Link Check** é uma ferramenta para checagem de links de servidores do Discord e também para encontrar links que estão escritos erroneamente. 

**Nota importante**: O uso excessivo dessa ferramenta pode levar a bloqueios de IP temporários ou permanentes. Portanto, não é recomendável o uso a não ser em situações bem específicas.

## Instalação

1. Clone o repositório:
   ```sh
   git clone https://github.com/e43b/DC-Server-Link-Check.git
   ```
2. Navegue até o diretório do projeto:
   ```sh
   cd DC-Server-Link-Check
   ```
3. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```

## Funcionalidades

### Check Invite

O script `checkinvite/codept.py` permite verificar se links de convite do Discord estão válidos ou inválidos. 

#### Como Usar

Para verificar a validade dos links de convite do Discord:
```sh
python checkinvite/codept.py
```

1. Execute o script.
2. Digite o link ou links de convite separados por vírgulas.
3. O script verificará na API do Discord e retornará se cada link é válido ou inválido.

### Link Finder

A ferramenta `findinvite/codept.py` tenta encontrar links de convite que foram escritos erroneamente. Se você tiver um link com os caracteres corretos, mas com erros de capitalização, este script pode ajudar.

#### Como Usar

Para encontrar um link de convite do Discord escrito erroneamente:
```sh
python findinvite/codept.py
```

1. Execute o script.
2. Digite o link de convite do Discord.
3. O script gerará todas as combinações possíveis de maiúsculas e minúsculas e testará cada uma na API até encontrar o link correto.

**Nota**: Esta ferramenta pode causar bloqueios devido ao número elevado de requisições, resultando no erro 429 (muitas requisições em um curto período de tempo). O script tem um cooldown de espera de 1 segundo entre as tentativas, mas o uso contínuo ou um número elevado de tentativas pode continuar causando bloqueios.

## Doações

Se você achar este projeto útil, considere fazer uma doação para apoiar o desenvolvimento contínuo: [Doe via Oxapay](https://oxapay.com/donate/40874860).

## Comunidade

Junte-se ao nosso servidor do Discord para discutir este projeto e obter suporte: [Servidor do Discord](https://discord.gg/CsBMMXBz7t).

---

**Nota**: Lembre-se sempre de usar essas ferramentas de maneira responsável e dentro dos limites das políticas de uso do Discord.
```

Este `README.md` fornece uma visão geral clara do projeto, como instalá-lo, usá-lo e onde obter suporte adicional ou contribuir com doações.
