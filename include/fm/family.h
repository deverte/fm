/**
 * \file fm/family.h
 * Indexed family, monad compherension (e.g. set comprehension (set-builder
 * notation, set abstraction), list comprehension).
 * 
 * \copyright GPL
 * \author Artem Shepelin (4.shepelin@gmail.com)
 */
#pragma once


#include <functional>


namespace fm {


/**
 * Indexed family, monad compherension (e.g. set comprehension (set-builder
 * notation, set abstraction), list comprehension).
 * 
 * \param lower_bound Lower bound index (including).
 * \param upper_bound Upper bound index (including).
 * \param f Intension.
 */
void family(int lower_bound, int upper_bound, std::function<void(int)> f) {
  for (int i = lower_bound; i <= upper_bound; i++) {
    f(i);
  }
}


}