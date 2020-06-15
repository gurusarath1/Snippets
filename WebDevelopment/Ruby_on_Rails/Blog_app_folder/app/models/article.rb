class Article < ApplicationRecord
  validates :title, presence: true, length: {minimun: 5}
end
