/**
 * @file Tags.hpp
 * @author snowapril (sinjihng@gmail.com)
 * @brief Common tags in the chess game
 * @version 0.1
 * @date 2021-07-23
 *
 * @copyright Copyright (c) 2021
 *
 */

#include <entt/entt.hpp>

namespace Commons
{
namespace Tags
{
using namespace entt::literals;
/**
 * @brief Represent player entity that can control piece & board
 */
using Player = entt::tag<"player"_hs>;
/**
 * @brief Represent chess piece which can move across the board on it's turn
 */
using Piece = entt::tag<"piece"_hs>;
/**
 * @brief Represent checkerboard where pieces can reside on
 */
using Board = entt::tag<"board"_hs>;
}  // namespace Tags
}  // namespace Commons