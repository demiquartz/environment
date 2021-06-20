/** @file
 * @brief ${main_brief}
 * @author ${name}
 * @copyright Copyright (c) ${year} ${name} &lt;${email}&gt; @n
 * Distributed under the MIT License (See accompanying file LICENSE
 * or copy at https://opensource.org/licenses/MIT)
 */
#include <iostream>
#include "version.hpp"

int main(int argc, char** argv) {
    std::cout << SYSNAME << " " << VERSION << std::endl;
    return EXIT_SUCCESS;
}
